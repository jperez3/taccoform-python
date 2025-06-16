module "python_terraform" {
  source = "../../module"

  environment = "prod"
  port        = 5678
}