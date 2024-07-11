# Databricks notebook source
# MAGIC %md
# MAGIC # Criando uma nova branch no Databricks
# MAGIC
# MAGIC Criar uma nova branch proporciona um ambiente controlado para desenvolver, testar e colaborar em alterações de código, garantindo ao mesmo tempo a segurança e a estabilidade do projeto como um todo.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Porquê preciso criar uma nova branch para meu usuário?
# MAGIC
# MAGIC Esta é uma prática recomendada por várias razões:
# MAGIC
# MAGIC **Isolamento de alterações**: Ao criar uma nova branch, você isola suas alterações do código principal ou de outras branches. Isso permite que você trabalhe em novos recursos, correções de bugs ou experimentos sem afetar diretamente o código existente.
# MAGIC
# MAGIC **Colaboração segura**: Se você estiver trabalhando em um ambiente de equipe, criar uma nova branch permite que outros membros da equipe vejam suas alterações antes de integrá-las ao código principal. Isso facilita a revisão de código e a colaboração entre os membros da equipe.
# MAGIC
# MAGIC **Facilidade de reversão**: Se suas alterações não funcionarem como esperado ou causarem problemas no código, você pode reverter facilmente para a versão anterior ao mesclar a branch principal. Isso ajuda a manter a estabilidade do código e a evitar interrupções no ambiente de produção.
# MAGIC
# MAGIC **Testes separados**: Você pode usar uma nova branch para realizar testes separados sem interferir no código principal. Isso é útil para garantir que suas alterações funcionem conforme o esperado antes de serem mescladas no ambiente de produção.
# MAGIC
# MAGIC **Experimentação e prototipagem**: Uma nova branch oferece um ambiente seguro para experimentar novas ideias ou prototipar recursos sem afetar o código principal. Isso é especialmente útil para desenvolvimento iterativo e inovação.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Para criar uma nova branch no Databricks, siga estas etapas:
# MAGIC
# MAGIC 1. **Acesse o Databricks**: Faça login na sua conta do Databricks.
# MAGIC
# MAGIC 2. **Abra o ambiente de desenvolvimento**: Navegue até o ambiente de desenvolvimento onde você deseja criar a nova branch. <https://dev.azure.com/bbts-lab/>
# MAGIC
# MAGIC 3. **Clique em "Git" ou "Version Control" na barra de ferramentas**: Geralmente, você encontrará essa opção na parte superior da interface do Databricks. Ex.: *Repos > Branches > New branch*
# MAGIC
# MAGIC 4. **Selecione a opção para criar uma nova branch**: Depois de acessar o controle de versão, haverá uma opção para criar uma nova branch. Geralmente, isso é feito clicando em um botão ou menu suspenso relacionado à gestão de branches.
# MAGIC
# MAGIC 5. **Dê um nome à nova branch**: Após selecionar a opção para criar uma nova branch, será solicitado que você forneça um nome para a nova branch. Escolha um nome descritivo que indique o propósito ou a natureza das alterações que você planeja fazer nessa branch.
# MAGIC
# MAGIC 6. **Confirme a criação da branch**: Após fornecer um nome, confirme a criação da nova branch. Isso pode envolver clicar em um botão de confirmação ou algo semelhante, dependendo da interface do Databricks.
# MAGIC
# MAGIC Depois de seguir essas etapas, você terá criado com sucesso uma nova branch no Databricks, onde poderá trabalhar e fazer alterações sem afetar diretamente a branch principal ou outras branches existentes. Certifique-se sempre de estar ciente das implicações de suas alterações e de como elas se relacionam com o fluxo de trabalho de desenvolvimento de sua equipe.
