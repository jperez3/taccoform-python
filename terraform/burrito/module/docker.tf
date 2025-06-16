resource "docker_image" "burrito" {
  name = "burrito-${var.environment}"
  build {
    path = "${path.module}/."
    dockerfile = "Dockerfile"
    tag  = ["burrito:${var.environment}"]

  }
}

resource "docker_container" "burrito" {
  name  = "burrito-${var.environment}"
  image = flatten(docker_image.burrito.build[*].tag)[0]
  ports {
      external = var.port
      internal = 5678
  }
  env = [
    "ECHO_TEXT='Hello from the ${var.environment} burrito!'",
  ]
}
