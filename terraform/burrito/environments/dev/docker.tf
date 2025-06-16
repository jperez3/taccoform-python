module "python_terraform" {
  source = "../../module"

  environment = "dev"
  port        = 4678
}