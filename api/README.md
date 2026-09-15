# Documentação de Estruturas de Dados - Compras Públicas e Contratações

Este documento apresenta a especificação e representação tabelar dos 5 objetos JSON fornecidos, estruturados na forma de **Dicionário de Dados** (schema de campos) e **Tabela de Dados (Registros)**.

---

## 1. Processo Licitatório / Ata (Resumo)

### 1.1. Dicionário de Dados (Campos)

| Campo | Tipo de Dado | Exemplo / Valor Original | Descrição |
| :--- | :--- | :--- | :--- |
| `ano` | Número (Integer) | `2025` | Ano do exercício do processo licitatório |
| `mes` | Número (Integer) | `7` | Mês do processo licitatório |
| `numeroProcesso` | Texto (String) | `"00.000.000000.2025"` | Número de identificação do processo administrativo |
| `nomeOrgao` | Texto (String) | `"SECRETARIA DE ESTADO EXEMPLO"` | Nome do órgão ou entidade contratante |
| `objeto` | Texto (String) | `"AQUISIÇÃO DE EQUIPAMENTOS"` | Descrição sucinta do objeto da licitação |
| `tipoProcesso` | Texto (String) | `"LICITAÇÃO"` | Categoria/Tipo do processo administrativo |
| `modalidade` | Texto (String) | `"PREGÃO ELETRÔNICO"` | Modalidade de licitação utilizada |
| `tipoJulgamento` | Texto (String) | `"MENOR PREÇO"` | Critério de julgamento das propostas |
| `situacao` | Texto (String) | `"HOMOLOGADO"` | Status/situação atual do procedimento licitatório |
| `dataCriacao` | Texto (Data/String) | `"2025-01-15"` | Data de autuação/criação do processo (YYYY-MM-DD) |
| `valorLicitado` | Número (Float/Currency) | `50000` | Valor total licitado/homologado (em R$) |
| `linkDocumentoAta` | Texto (URL/String) | `"https://exemplo.com/documento.pdf"` | Link direto para o documento oficial ou Ata |

### 1.2. Visualização dos Dados em Tabela

| Ano | Mês | Nº Processo | Nome do Órgão | Objeto | Tipo Processo | Modalidade | Tipo Julgamento | Situação | Data Criação | Valor Licitado (R$) | Link Documento/Ata |
| :-: | :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :-: | :-: | :--- |
| 2025 | 7 | 00.000.000000.2025 | SECRETARIA DE ESTADO EXEMPLO | AQUISIÇÃO DE EQUIPAMENTOS | LICITAÇÃO | PREGÃO ELETRÔNICO | MENOR PREÇO | HOMOLOGADO | 2025-01-15 | R$ 50.000,00 | [Ata/Documento](https://exemplo.com/documento.pdf) |

---

## 2. Detalhes da Licitação

### 2.1. Dicionário de Dados (Campos)

| Campo | Tipo de Dado | Exemplo / Valor Original | Descrição |
| :--- | :--- | :--- | :--- |
| `numeroProcesso` | Texto (String) | `"string"` | Número do processo administrativo associado |
| `numeroLicitacao` | Texto (String) | `"string"` | Número de identificação da licitação |
| `cadastroCge` | Texto (String) | `"string"` | Código de registro/cadastro na CGE |
| `tipoDocumento` | Texto (String) | `"string"` | Tipo de documento emitido/vinculado |
| `nomeOrgao` | Texto (String) | `"string"` | Nome do órgão promotor da licitação |
| `objeto` | Texto (String) | `"string"` | Descrição detalhada do objeto da licitação |
| `modalidade` | Texto (String) | `"string"` | Modalidade da licitação (ex: Pregão, Concorrência) |
| `tipoLicitacao` | Texto (String) | `"string"` | Classificação do tipo de licitação |
| `criterioClassificacao` | Texto (String) | `"string"` | Critério para classificação dos participantes |
| `situacao` | Texto (String) | `"string"` | Situação atual da licitação (ex: Em Aberto, Homologado) |
| `dataCriacao` | Texto (Data/String) | `"string"` | Data de criação/publicação (YYYY-MM-DD) |
| `dataAbertura` | Texto (Data/String) | `"string"` | Data da sessão de abertura de propostas |
| `dataAdjudicacao` | Texto (Data/String) | `"string"` | Data de adjudicação do objeto |
| `valorEstimado` | Número (Float) | `0` | Valor total estimado do certame |
| `valorAdjudicado` | Número (Float) | `0` | Valor total final adjudicado |
| `numParticipantes` | Número (Integer) | `0` | Quantidade de fornecedores participantes |
| `registroPreco` | Texto (String) | `"string"` | Indica se é Sistema de Registro de Preços (Sim/Não) |
| `amparoLegal` | Texto (String) | `"string"` | Legislação/base legal aplicável |
| `urlEdital` | Texto (URL/String) | `"string"` | URL de acesso ao Edital completo |
| `urlContratacao` | Texto (URL/String) | `"string"` | URL do termo de contratação |
| `urlPncp` | Texto (URL/String) | `"string"` | Link da publicação no Portal Nacional de Contratações Públicas |
| `documentos` | Texto (String) | `"string"` | Relação/anexos de documentos vinculados |
| `participantes` | Texto (String) | `"string"` | Relação de empresas/participantes inscritos |

### 2.2. Visualização dos Dados em Tabela

| Nº Processo | Nº Licitação | Cad. CGE | Tipo Doc. | Nome do Órgão | Objeto | Modalidade | Tipo Licitação | Critério Classif. | Situação | Data Criac. | Data Abert. | Data Adjud. | Valor Estim. | Valor Adjud. | Nº Part. | Reg. Preço | Amparo Legal | Link Edital | Link Contrat. | Link PNCP | Documentos | Participantes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :-: | :-: | :-: | :-: | :-: | :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| string | string | string | string | string | string | string | string | string | string | string | string | string | 0.00 | 0.00 | 0 | string | string | string | string | string | string | string |

---

## 3. Contratos Administrativos

### 3.1. Dicionário de Dados (Campos)

| Campo | Tipo de Dado | Exemplo / Valor Original | Descrição |
| :--- | :--- | :--- | :--- |
| `anoInicioVigencia` | Número (Integer) | `2025` | Ano de início da vigência do contrato |
| `registroCge` | Texto (String) | `"string"` | Número do registro junto à Controladoria Geral |
| `numeroContrato` | Texto (String) | `"string"` | Número do contrato administrativo |
| `numeroProcessoLicitacao` | Texto (String) | `"string"` | Número do processo licitatório de origem |
| `nomeOrgao` | Texto (String) | `"string"` | Nome do órgão contratante |
| `siglaOrgao` | Texto (String) | `"string"` | Sigla do órgão contratante |
| `codigoOrgao` | Texto (String) | `"string"` | Código de identificação do órgão |
| `municipio` | Texto (String) | `"string"` | Município de execução do contrato |
| `objeto` | Texto (String) | `"string"` | Objeto do contrato |
| `objetoComplemento` | Texto (String) | `"string"` | Detalhamento ou complemento do objeto |
| `contratado` | Texto (String) | `"string"` | Nome/Razão Social da empresa contratada |
| `cnpjCpf` | Texto (String) | `"string"` | CNPJ ou CPF do fornecedor contratado |
| `dataAssinatura` | Texto (Data/String) | `"2025-01-01"` | Data de assinatura do instrumento contratual |
| `dataPublicacao` | Texto (Data/String) | `"string"` | Data da publicação oficial do contrato |
| `dataInicioVigencia` | Texto (Data/String) | `"string"` | Data de início da vigência contratual |
| `dataTerminoVigencia` | Texto (Data/String) | `"string"` | Data do término da vigência contratual |
| `valorOriginal` | Número (Float) | `0` | Valor pactuado originalmente no contrato |
| `valorAditivos` | Número (Float) | `0` | Valor somado de termos aditivos |
| `valorApostilas` | Número (Float) | `0` | Valor somado de apostilamentos |
| `valorTotal` | Número (Float) | `0` | Valor total atualizado do contrato |
| `emergencial` | Texto (String) | `"string"` | Indicador de contratação emergencial (Sim/Não) |
| `urlContrato` | Texto (URL/String) | `"string"` | Link para visualização do documento do contrato |
| `aditivo` | Texto (String) | `"string"` | Informações sobre aditivos firmados |
| `nomeGestor` | Texto (String) | `"string"` | Nome do gestor responsável pelo contrato |
| `matriculaGestor` | Texto (String) | `"string"` | Matrícula funcional do gestor |
| `cpfGestor` | Texto (String) | `"***.123.456-**"` | CPF do gestor do contrato (mascarado/anonimizado) |
| `dataPortaria` | Texto (Data/String) | `"2025-01-01"` | Data de emissão da portaria de designação do gestor |
| `numeroPortariaGestor` | Texto (String) | `"string"` | Número da portaria de designação do gestor |

### 3.2. Visualização dos Dados em Tabela

#### Tabela A: Informações do Contrato e Contratado
| Ano Vig. | Reg. CGE | Nº Contrato | Proc. Licitação | Órgão (Sigla/Cód.) | Município | Objeto / Detalhe | Contratado | CNPJ/CPF |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2025 | string | string | string | string (string / string) | string | string - string | string | string |

#### Tabela B: Datas, Valores e Gestão
| Data Assin. | Data Pub. | Vigência (Início - Fim) | Valor Orig. | Aditivos | Apostilas | Valor Total | Emergencial | Gestor (CPF/Matrícula) | Portaria (Nº / Data) | Link Contrato |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- | :--- | :--- |
| 2025-01-01 | string | string a string | 0,00 | 0,00 | 0,00 | 0,00 | string | string (***.123.456-** / string) | string (2025-01-01) | string |

---

## 4. Itens do Processo Licitatório e Fornecedores

### 4.1. Dicionário de Dados (Campos)

| Campo | Tipo de Dado | Exemplo / Valor Original | Descrição |
| :--- | :--- | :--- | :--- |
| `ano` | Número (Integer) | `2025` | Ano de referência do item no processo |
| `descricao` | Texto (String) | `"string"` | Descrição detalhada do bem ou serviço |
| `quantidade` | Número (Float/Int) | `0` | Quantidade licitada do item |
| `unidadeMedida` | Texto (String) | `"string"` | Unidade de medida (ex: UN, KG, CAIXA, M) |
| `valorUnitarioEstimado` | Número (Float) | `0` | Valor unitário estimado pela administração |
| `valorTotalEstimado` | Número (Float) | `0` | Valor total estimado (Qtd x Valor Unit. Estimado) |
| `valorUnitarioHomologado` | Número (Float) | `0` | Valor unitário final homologado/vencedor |
| `tipoPessoa` | Texto (String) | `"string"` | Tipo de pessoa do fornecedor (Física / Jurídica) |
| `cpfCnpjFornecedor` | Texto (String) | `"string"` | CPF ou CNPJ do fornecedor homologado |
| `razaoSocialFornecedor` | Texto (String) | `"string"` | Nome ou Razão Social do fornecedor vencedor |
| `nuProcesso` | Texto (String) | `"string"` | Número do processo licitatório ao qual o item pertence |

### 4.2. Visualização dos Dados em Tabela

| Ano | Nº Processo | Descrição do Item | Qtd | Unid. | Val. Unit. Estimado | Val. Total Estimado | Val. Unit. Homologado | Tipo Pessoa | CPF/CNPJ Fornecedor | Razão Social Fornecedor |
| :-: | :--- | :--- | :-: | :-: | :-: | :-: | :-: | :-: | :--- | :--- |
| 2025 | string | string | 0 | string | 0,00 | 0,00 | 0,00 | string | string | string |

---

## 5. Plano de Contratações Anual (PCA)

### 5.1. Dicionário de Dados (Campos)

| Campo | Tipo de Dado | Exemplo / Valor Original | Descrição |
| :--- | :--- | :--- | :--- |
| `ano` | Número (Integer) | `2026` | Ano de planejamento do PCA |
| `cnpjOrgao` | Texto (String) | `"string"` | CNPJ do órgão solicitante |
| `nomeOrgao` | Texto (String) | `"string"` | Nome do órgão promotor |
| `unidade` | Texto (String) | `"string"` | Unidade administrativa requisitante |
| `idItemPca` | Texto (String) | `"string"` | Identificador único do item no PCA |
| `categoriaItem` | Texto (String) | `"string"` | Categoria do item (ex: Bens, Serviços, Obras) |
| `classeGrupo` | Texto (String) | `"string"` | Código/Nome da Classe ou Grupo do catálogo |
| `codigoItem` | Texto (String) | `"string"` | Código do item no catálogo de compras (CATMAT/CATSER) |
| `descricaoItem` | Texto (String) | `"string"` | Descrição detalhada do item planejado |
| `unidadeFornecimento` | Texto (String) | `"string"` | Unidade de fornecimento padrão |
| `quantidade` | Número (Float/Int) | `0` | Quantidade estimada a ser adquirida |
| `valorUnitario` | Número (Float) | `0` | Valor unitário estimado |
| `valorTotal` | Número (Float) | `0` | Valor total estimado do item |
| `valorOrcamentoExercicio` | Número (Float) | `0` | Valor orçamentário alocado para o exercício |
| `dataDesejada` | Texto (Data/String) | `"2026-01-01"` | Data estimada/desejada para a contratação |
| `linkPca` | Texto (URL/String) | `"https://exemplo.gov.br/pca"` | Link para o Plano de Contratações Anual completo |
| `linkItemPca` | Texto (URL/String) | `"https://exemplo.gov.br/pca/item"` | Link direto para o item no PCA |

### 5.2. Visualização dos Dados em Tabela

| Ano | CNPJ / Órgão / Unidade | ID Item PCA | Categoria / Classe | Cód. Item | Descrição do Item | Unid. Fornecimento | Qtd | Val. Unit. | Val. Total | Orçamento Exercício | Data Desejada | Links |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :-: | :-: | :-: | :-: | :-: | :--- |
| 2026 | string - string (string) | string | string / string | string | string | string | 0 | 0,00 | 0,00 | 0,00 | 2026-01-01 | [PCA](https://exemplo.gov.br/pca) \| [Item](https://exemplo.gov.br/pca/item) |
