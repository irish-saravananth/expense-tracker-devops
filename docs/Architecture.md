# Architecture Documentation

## Overview

The **Smart Expense Tracker Platform** is designed as a cloud-native, containerized application following modern DevOps principles. The project demonstrates how an application progresses from source code to a fully automated deployment on Kubernetes while maintaining scalability, observability, and maintainability.

Although initially deployed as a modular monolithic application, the architecture is intentionally structured to support future migration to a microservices-based design with minimal refactoring.

---

# System Architecture

```text
                     Developer
                         │
                         ▼
                      Git Commit
                         │
                         ▼
                      GitHub
                         │
                         ▼
               Azure DevOps Pipeline
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
      ▼                  ▼                  ▼
 Code Validation    Docker Build     Infrastructure
                                         │
                                         ▼
                                     Terraform
                                         │
                                         ▼
                                      Kubernetes
                                         │
         ┌───────────────────────────────┼──────────────────────────────┐
         ▼                               ▼                              ▼
   React Frontend                 Flask Backend                   PostgreSQL
         │                               │                              │
         └───────────────────────┬───────┘                              │
                                 ▼                                      │
                          Prometheus Metrics                            │
                                 │                                      │
                                 ▼                                      │
                              Grafana                                   │
                                 │                                      │
                                 ▼                                      │
                                Loki ◄──────────────────────────────────┘
```

---

# Architecture Principles

The project is designed around the following principles:

* Modular application design
* Infrastructure as Code (IaC)
* Immutable container deployments
* Automated CI/CD
* Kubernetes-native deployments
* Centralized monitoring
* Centralized logging
* Version-controlled infrastructure
* Repeatable deployments

---

# Component Responsibilities

## Frontend

Responsibilities:

* Responsive user interface
* Authentication
* Dashboard
* Expense management
* API communication
* Input validation

Technology:

* React
* Material UI
* Axios

---

## Backend API

Responsibilities:

* Business logic
* Authentication
* Authorization
* REST API
* Database operations
* Metrics exposure
* Logging

Technology:

* Python
* Flask
* SQLAlchemy
* JWT Authentication

---

## Database

Responsibilities:

* Store application data
* Maintain relationships
* Persistent storage

Technology:

* PostgreSQL

---

## Docker

Responsibilities:

* Build reproducible images
* Standardize runtime environment
* Simplify deployments

Images:

* Frontend
* Backend
* Database

---

## Kubernetes

Responsibilities:

* Container orchestration
* Service discovery
* Scaling
* Self-healing
* Rolling updates
* Secret management

Resources to be managed:

* Namespace
* Deployment
* Service
* ConfigMap
* Secret
* Persistent Volume Claim
* Ingress

---

## Terraform

Responsibilities:

* Provision Kubernetes resources
* Maintain declarative infrastructure
* Version infrastructure changes

---

## Ansible

Responsibilities:

* Configure development environment
* Install dependencies
* Automate deployment tasks
* Execute operational playbooks

---

## Azure DevOps

Responsibilities:

* Continuous Integration
* Continuous Deployment
* Automated testing
* Docker image creation
* Deployment automation

---

## Prometheus

Responsibilities:

* Collect application metrics
* Collect Kubernetes metrics
* Monitor infrastructure health

---

## Grafana

Responsibilities:

* Visualize metrics
* Build operational dashboards
* Support troubleshooting

---

## Loki

Responsibilities:

* Centralize application logs
* Aggregate container logs
* Simplify log analysis

---

# Request Flow

```text
User
 │
 ▼
React Frontend
 │
 ▼
Flask REST API
 │
 ▼
PostgreSQL
 │
 ▼
Response
 │
 ▼
Frontend
```

---

# Deployment Flow

```text
Developer
      │
      ▼
Git Push
      │
      ▼
GitHub
      │
      ▼
Azure DevOps
      │
      ▼
Docker Build
      │
      ▼
Container Registry
      │
      ▼
Terraform
      │
      ▼
Kubernetes
      │
      ▼
Application Available
```

---

# Monitoring Flow

```text
Application
      │
      ▼
Prometheus
      │
      ▼
Grafana
```

---

# Logging Flow

```text
Application Logs
        │
        ▼
      Loki
        │
        ▼
    Grafana
```

---

# Repository Structure

```text
backend/         Application source code
frontend/        React application
database/        Database scripts
docker/          Dockerfiles and container assets
kubernetes/      Kubernetes manifests
terraform/       Infrastructure as Code
ansible/         Configuration management
monitoring/      Monitoring configuration
scripts/         Utility scripts
docs/            Project documentation
tests/           Automated tests
```

---

# Scalability Considerations

The architecture is designed to support future enhancements, including:

* Horizontal pod autoscaling
* Multi-node Kubernetes clusters
* External container registries
* Cloud-managed Kubernetes services
* GitOps workflows
* Service mesh integration
* Centralized secret management
* Distributed tracing

---

# Design Decisions

This project intentionally uses:

* Kubernetes (Kind) for local orchestration
* Terraform for declarative infrastructure
* Ansible for host and environment automation
* Azure DevOps for CI/CD
* Docker for packaging
* PostgreSQL for persistence
* Prometheus and Grafana for observability
* Loki for centralized logging

These technologies reflect common enterprise DevOps practices while remaining accessible in a local development environment.

---

# Future Architecture Enhancements

As the project evolves, planned improvements include:

* Kubernetes Ingress Controller
* HTTPS with TLS
* GitOps deployment model
* Container image scanning
* Secret management integration
* Policy-as-Code
* High availability database deployment
* Multi-environment support (Development, Staging, Production)
* Automated disaster recovery testing