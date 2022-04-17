CREATE TABLE "Aluguel"(
    "id" INTEGER NOT NULL,
    "id_imovel" INTEGER NOT NULL,
    "id_inquilino" INTEGER NOT NULL,
    "id_corretor" INTEGER NOT NULL,
    "valor" INTEGER NOT NULL
);
ALTER TABLE
    "Aluguel" ADD PRIMARY KEY("id");
CREATE TABLE "Contrato"(
    "id" INTEGER NOT NULL,
    "id_aluguel" INTEGER NOT NULL,
    "duracao" INTEGER NOT NULL
);
ALTER TABLE
    "Contrato" ADD PRIMARY KEY("id");
CREATE TABLE "Imóvel"(
    "id" INTEGER NOT NULL,
    "logradouro" VARCHAR(255) NOT NULL,
    "cep" INTEGER NOT NULL,
    "bairro" VARCHAR(255) NOT NULL,
    "cidade" VARCHAR(255) NOT NULL,
    "id_proprietario" INTEGER NOT NULL
);
ALTER TABLE
    "Imóvel" ADD PRIMARY KEY("id");
CREATE TABLE "Proprietário"(
    "nome" VARCHAR(255) NOT NULL,
    "data_nascimento" DATE NOT NULL,
    "id" INTEGER NOT NULL
);
ALTER TABLE
    "Proprietário" ADD PRIMARY KEY("id");
CREATE TABLE "Corretor"(
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "data_nascimento" DATE NOT NULL
);
ALTER TABLE
    "Corretor" ADD PRIMARY KEY("id");
CREATE TABLE "Inquilino"(
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "data_nascimento" DATE NOT NULL
);
ALTER TABLE
    "Inquilino" ADD PRIMARY KEY("id");
ALTER TABLE
    "Contrato" ADD CONSTRAINT "contrato_id_aluguel_foreign" FOREIGN KEY("id_aluguel") REFERENCES "Aluguel"("id");
ALTER TABLE
    "Corretor" ADD CONSTRAINT "corretor_nome_foreign" FOREIGN KEY("nome") REFERENCES "Aluguel"("id");
ALTER TABLE
    "Aluguel" ADD CONSTRAINT "aluguel_id_imovel_foreign" FOREIGN KEY("id_imovel") REFERENCES "Imóvel"("id");
ALTER TABLE
    "Imóvel" ADD CONSTRAINT "imóvel_id_proprietario_foreign" FOREIGN KEY("id_proprietario") REFERENCES "Proprietário"("id");
ALTER TABLE
    "Aluguel" ADD CONSTRAINT "aluguel_id_inquilino_foreign" FOREIGN KEY("id_inquilino") REFERENCES "Inquilino"("id");