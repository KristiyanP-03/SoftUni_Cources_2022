
# !!! Дава ми грешка, че не намира values.tfvars, а е в същата директория

variable "resource_group_name" {
  type        = string
  description = "The name of the resource group."
  default     = "kristiyanpisevurlshortenerrg"
}

variable "resource_group_location" {
  type        = string
  description = "The location for the resource group."
  default     = "West Europe"
}

variable "app_service_plan_name" {
  type        = string
  description = "The name of the App Service Plan."
  default     = "kristiyanpisevurlhortenersp"
}

variable "app_service_name" {
  type        = string
  description = "The name of the Azure App Service."
  default     = "kristiyanpisevurlshortener"
}

variable "sql_server_name" {
  type        = string
  description = "The name of the SQL Server."
  default     = "kristiyanpisevurlhortenersqlerver"
}

variable "sql_database_name" {
  type        = string
  description = "The name of the SQL database."
  default     = "mydatabase"
}

variable "sql_admin_login" {
  type        = string
  description = "The SQL Server administrator login."
  default     = "4dm1n157r470r"
}

variable "sql_admin_password" {
  type        = string
  description = "The SQL Server administrator password."
  default     = "4-v3ry-53cr37-p455w0rd"
}

variable "firewall_rule_name" {
  type        = string
  description = "The name of the firewall rule."
  default     = "firewall"
}

variable "repo_URL" {
  type        = string
  description = "The URL of the repository."
  default     = "https://github.com/KristiyanP-03/URLShortener"
}
