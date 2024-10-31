CREATE TABLE "orders" (
  "order_id" integer PRIMARY KEY NOT NULL,
  "order_status" "enum(Iniciado,Em andamento,Finalizado)",
  "created_at" timestamp DEFAULT 'now()',
  "created_by" varchar,
  "o_client_id" integer NOT NULL,
  "o_product_id" integer NOT NULL,
  "o_payments_id" integer,
  "price" float,
  "updated_at" timestamp DEFAULT 'now()',
  "quantity" integer NOT NULL
);

CREATE TABLE "products" (
  "product_id" integer PRIMARY KEY NOT NULL,
  "product_name" varchar NOT NULL,
  "product_status" enum(Ativo,Inativo),
  "product_category" varchar,
  "product_description" varchar,
  "product_situation" enum(Antigo,Novo),
  "quantity" integer NOT NULL DEFAULT 0
);

CREATE TABLE "clients" (
  "client_id" integer PRIMARY KEY NOT NULL,
  "client_name" varchar NOT NULL,
  "client_email" varchar UNIQUE NOT NULL,
  "client_address" varchar,
  "client_cpf" varchar(11) UNIQUE,
  "client_rg" varchar(9) UNIQUE,
  "client_phonenumber" varchar(11) UNIQUE,
  "client_created_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "payments" (
  "order_id" integer,
  "payments_id" integer PRIMARY KEY NOT NULL,
  "payment_method" enum(Pix,Débito,Crédito),
  "payment_created_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "categories" (
  "category_id" integer PRIMARY KEY NOT NULL,
  "category_name" varchar UNIQUE NOT NULL,
  "category_description" varchar
);

CREATE TABLE "employees" (
  "employee_id" integer PRIMARY KEY NOT NULL,
  "employee_name" varchar NOT NULL,
  "employee_email" varchar,
  "employee_address" varchar,
  "employee_cpf" varchar(11) UNIQUE,
  "employee_rg" varchar(9) UNIQUE,
  "employee_phonenumber" varchar(11) UNIQUE,
  "employee_created_at" timestamp DEFAULT 'now()'
);

ALTER TABLE "orders" ADD FOREIGN KEY ("o_client_id") REFERENCES "clients" ("client_id");

ALTER TABLE "orders" ADD FOREIGN KEY ("o_product_id") REFERENCES "products" ("product_id");

ALTER TABLE "orders" ADD FOREIGN KEY ("o_payments_id") REFERENCES "payments" ("payments_id");

ALTER TABLE "products" ADD FOREIGN KEY ("product_category") REFERENCES "categories" ("category_id");

ALTER TABLE "payments" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("order_id");
