terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file("my-creds.json")  # <-- ОСЬ ЦЬОГО РЯДКА НЕ ВИСТАЧАЄ
  project     = "driven-country-243417"
  region      = "us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "dtc-de-bucket-driven-country-243417" # <-- Ваше унікальне ім'я
  location      = "US"
  

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

# 2. Створення Датасету (BigQuery Dataset)
resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = "trips_data_all"
  location   = "US"
}