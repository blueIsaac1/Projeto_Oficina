--  Definindo enum's
CREATE TYPE order_status AS ENUM ('Iniciado', 'Em andamento', 'Finalizado');
CREATE TYPE product_status AS ENUM ('Ativo', 'Inativo');
CREATE TYPE product_situation AS ENUM ('Antigo', 'Novo');
CREATE TYPE payment_method AS ENUM ('Pix', 'Débito', 'Crédito');

-- Indices para consultas
CREATE INDEX idx_client_email ON clients(client_email);
CREATE INDEX idx_employee_email ON employees(employee_email);
CREATE INDEX idx_orders_created_at ON orders(created_at);

CREATE TABLE "clients" (
  "client_id" serial PRIMARY KEY,
  "client_name" varchar NOT NULL,
  "client_email" varchar UNIQUE NOT NULL,
  "client_address" varchar,																																																																									
  "client_cpf" varchar(11) UNIQUE,
  "client_rg" varchar(9) UNIQUE,
  "client_phonenumber" varchar(11) UNIQUE,
  "client_created_at" timestamp DEFAULT now()
);

CREATE TABLE "categories" (
  "category_id" serial PRIMARY KEY,
  "category_name" varchar UNIQUE NOT NULL,
  "category_description" varchar
);

CREATE TABLE "products" (
  "product_id" serial PRIMARY KEY,
  "product_name" varchar NOT NULL,
  "product_status" product_status DEFAULT 'Ativo',
  "product_category" integer REFERENCES "categories" ("category_id"),
  "product_description" varchar,
  "product_situation" product_situation DEFAULT 'Novo',
  "quantity" integer NOT NULL DEFAULT 0
);


CREATE TABLE "employees" (
  "employee_id" serial PRIMARY KEY,
  "employee_name" varchar NOT NULL,
  "employee_email" varchar,
  "employee_address" varchar,
  "employee_cpf" varchar(11) UNIQUE,
  "employee_rg" varchar(9) UNIQUE,
  "employee_phonenumber" varchar(11) UNIQUE,
  "employee_created_at" timestamp DEFAULT now()
);

CREATE TABLE "orders" (
  "order_id" serial PRIMARY KEY,
  "order_status" order_status DEFAULT 'Iniciado',
  "created_at" timestamp DEFAULT now(),
  "created_by" varchar, -- funcionario ou admin?
  "client_id" integer NOT NULL REFERENCES "clients" ("client_id"),
  "product_id" integer NOT NULL REFERENCES "products" ("product_id"),
  "payments_id" integer NOT NULL REFERENCES "payments" ("payments_id"),
  "price" float,
  "updated_at" timestamp DEFAULT now(),
  "quantity" integer NOT NULL
);

CREATE TABLE "payments" (
  "order_id" integer,
  "payments_id" serial PRIMARY KEY,
  "payment_method" payment_method,
  "payment_created_at" timestamp DEFAULT now()
);

-- Checagens básicas
ALTER TABLE clients ADD CONSTRAINT chk_client_cpf_length CHECK (LENGTH(client_cpf) = 11);
ALTER TABLE clients ADD CONSTRAINT chk_client_phone_length CHECK (LENGTH(client_phonenumber) = 11);

-- ALTER TABLE "orders" ADD FOREIGN KEY ("o_client_id") REFERENCES "clients" ("client_id"); -- ligação cliente indentificando no orders

-- ALTER TABLE "orders" ADD FOREIGN KEY ("o_product_id") REFERENCES "products" ("product_id"); -- ligação produto indentificando no orders

-- ALTER TABLE "orders" ADD FOREIGN KEY ("o_payments_id") REFERENCES "payments" ("payments_id"); -- ligação pagamento indentificando no orders

-- ALTER TABLE "products" ADD FOREIGN KEY ("product_category") REFERENCES "categories" ("category_id"); -- ligação categoria produto com o id da categoria raiz

ALTER TABLE "payments" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("order_id"); -- cada pagamento tem uma order referenciada


-- Inserindo dados na tabela clients
INSERT INTO clients (client_name, client_email, client_address, client_cpf, client_rg, client_phonenumber)
VALUES 
('João Silva', 'joao.silva@example.com', 'Rua A, 123', '12345678901', 'RG1234567', '11987654321'),
('Maria Oliveira', 'maria.oliveira@example.com', 'Rua B, 456', '98765432100', 'RG7654321', '11912345678');

-- Inserindo dados na tabela employees
INSERT INTO employees (employee_name, employee_email, employee_address, employee_cpf, employee_rg, employee_phonenumber)
VALUES 
('Carlos Pereira', 'carlos.pereira@example.com', 'Avenida C, 789', '11223344556', 'RG2345678', '11876543210'),
('Ana Costa', 'ana.costa@example.com', 'Praça D, 101', '66554433221', 'RG3456789', '11812345678');

-- Inserindo dados na tabela categories
INSERT INTO categories (category_name, category_description)
VALUES 
('Eletrônicos', 'Dispositivos eletrônicos e gadgets'),
('Roupas', 'Vestimentas e acessórios');

-- Inserindo dados na tabela products
INSERT INTO products (product_name, product_status, product_category, product_description, product_situation, quantity)
VALUES 
('Smartphone XYZ', 'Ativo', 1, 'Smartphone com 128GB de armazenamento', 'Novo', 50),
('Camiseta Estampada', 'Ativo', 2, 'Camiseta de algodão com estampas divertidas', 'Novo', 100);

-- Inserindo dados na tabela payments
INSERT INTO payments (order_id, payment_method)
VALUES 
(1, 'Pix'),
(2, 'Débito');

-- Atualizando os pedidos para adicionar os payments_id agora
UPDATE orders SET payments_id = 1 WHERE order_id = 1;
UPDATE orders SET payments_id = 2 WHERE order_id = 2;

-- Inserindo dados na tabela orders
INSERT INTO orders (order_status, created_at, created_by, client_id, product_id, payments_id, price, quantity)
VALUES 
('Iniciado', now(), 1, 1, 1, 1, 999.99, 2), -- João Silva comprando 2 Smartphones
('Finalizado', now(), 2, 2, 2, 2, 49.90, 1); -- Maria Oliveira comprando 1 Camiseta

-- Testes
 
SELECT 
    o.order_id,
    o.order_status,
    o.created_at,
    o.created_by,
    c.client_name,
    c.client_email,
    p.product_name,
    o.price,
    o.quantity
FROM 
    orders o
JOIN 
    clients c ON o.client_id = c.client_id
JOIN 
    products p ON o.product_id = p.product_id;

--
SELECT 
    pay.payments_id,
    pay.payment_method,
    pay.payment_created_at,
    o.order_id,
    o.order_status,
    o.price,
    c.client_name,
    c.client_email
FROM 
    payments pay
JOIN 
    orders o ON pay.order_id = o.order_id
JOIN 
    clients c ON o.client_id = c.client_id;

--
SELECT 
    p.product_id,
    p.product_name,
    p.product_status,
    p.product_description,
    c.category_name
FROM 
    products p
JOIN 
    categories c ON p.product_category = c.category_id;

--
SELECT 
    p.product_name,
    SUM(o.quantity) AS total_quantity_sold,
    SUM(o.price * o.quantity) AS total_sales_value
FROM 
    orders o
JOIN 
    products p ON o.product_id = p.product_id
GROUP BY 
    p.product_name;
	
--
SELECT 
    p.product_id,
    p.product_name,
    p.quantity,
    p.product_status
FROM 
    products p
WHERE 
    p.product_status = 'Ativo';

--
SELECT 
    c.client_name,
    c.client_email,
    o.order_id,
    o.order_status
FROM 
    clients c
LEFT JOIN 
    orders o ON c.client_id = o.client_id;
