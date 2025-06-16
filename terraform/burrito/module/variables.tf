variable "environment" {
  description = "The environment for the Burrito module, e.g., dev, prod."
  type        = string
  
}

variable "port" {
  description = "The external port to expose for the Docker container."
  type        = number
  default     = 5678
  
}