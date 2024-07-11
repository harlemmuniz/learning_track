locals {
  storage_account_files = fileset("./storage_accounts/", "*.json")
  storage_account_data  = [for f in local.storage_account_files : jsondecode(file("./storage_accounts/${f}"))]

  storage_container_files = fileset("./storage_containers/", "*.json")
  storage_container_data  = [for f in local.storage_container_files : jsondecode(file("./storage_containers/${f}"))]
}

module "storage_account_module" {
  source                   = "./modules/storage_account"
  
  for_each = {for f in local.storage_account_data : f.name => f if f.type == "Microsoft.Storage/storageAccounts"}

  name                     = "${trimsuffix(each.value.name, "lab")}${var.ambiente}"
  location                 = var.location
  resource_group_name      = var.resource_group_name
  account_tier             = each.value.sku.tier
  account_replication_type = trimprefix(each.value.sku.name, "Standard_")

  tags = lookup(each.value, "tags", null)
}

module "storage_container_module" {
  source                = "./modules/storage_container"

  for_each = {for f in local.storage_container_data : f.name => f if f.type == "Microsoft.Storage/storageContainer"}

  name                  = each.value.name
  #storage_account_name  = module.storage_account_module.name
  storage_account_name  = "datalaketemplab"
  container_access_type = "private"

  depends_on = [ module.storage_account_module ]
}
