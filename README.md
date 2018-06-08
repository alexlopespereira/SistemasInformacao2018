# SistemasInformacao2018
Repositorio do curso de Sistemas de Informação / ENAP no ano de 2018.

id,cod_org_superior,nome_org_superior,cod_orgao_subordinado,nome_org_subordinado,cod_unid_gestora,nome_unid_gestora,cod_funcao,nome_funcao,cod_subfuncao,nome_subfuncao,cod_programa,nome_programa,cod_acao,nome_acao,linguagem_cidada,cpf_favorecido,nome_favorecido,doc_pagamento,gestao_pagamento,data_pagamento,valor_pagamento

select nome_org_subordinado, nome_unid_gestora, nome_favorecido, substr(data_pagamento, -4) as ano, sum(valor_pagamento) as total
from diarias
group by nome_favorecido, ano
order by total desc;
--limit 40;

select * from diarias limit 3;
select distinct nome_acao from diarias limit 10;
select * from diarias where nome_favorecido like 'Osamu%';

select distinct substr(data_pagamento, -4) from diarias;

select nome_org_subordinado, nome_unid_gestora, substr(data_pagamento, -4) as ano, sum(valor_pagamento) as total
from diarias
group by nome_unid_gestora, ano
order by total desc;
--limit 40;


CREATE table public.diarias_unid_gestoras AS
 SELECT d.nome_org_subordinado,
    d.nome_unid_gestora,
    d.ano,
    u.qtd_favorecidos,
    sum(d.valor_pagamento) AS total
   FROM diarias d
     JOIN tabela_unidade_gestora u ON u.cod_unid_gestora = d.cod_unid_gestora AND d.ano = u.ano
  GROUP BY d.nome_org_subordinado, d.nome_unid_gestora, u.qtd_favorecidos, d.ano
  ORDER BY (sum(d.valor_pagamento)) DESC;

ALTER TABLE public.diarias_unid_gestoras
  OWNER TO aluno;