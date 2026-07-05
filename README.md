# 🚀 Smart Expense Tracker Platform - Enterprise DevOps Project

> An end-to-end enterprise-grade DevOps project demonstrating modern CI/CD, Infrastructure as Code, Kubernetes, Configuration Management, Monitoring, and Observability using open-source tools.

---

# 📌 Project Overview

The **Smart Expense Tracker Platform** is a responsive web application designed for both desktop and mobile users. Beyond the application itself, the primary goal of this repository is to demonstrate how a production-ready application can be built, tested, containerized, deployed, monitored, and managed using modern DevOps practices.

This project is intended as a portfolio showcasing practical experience with enterprise DevOps tools and workflows.

---

# 🎯 Project Objectives

* Build a production-ready web application
* Implement Continuous Integration and Continuous Deployment (CI/CD)
* Deploy applications to Kubernetes
* Automate infrastructure using Terraform
* Automate configuration management using Ansible
* Monitor infrastructure and applications using Prometheus and Grafana
* Centralize logs using Loki
* Follow Git branching and release management best practices
* Document every stage of the project

---

# 🏗️ High-Level Architecture

```text
Developer
    │
    ▼
Git
    │
    ▼
GitHub
    │
    ▼
Azure DevOps Pipeline
    │
    ├── Build
    ├── Test
    ├── Docker Image
    ├── Infrastructure Provisioning
    ├── Kubernetes Deployment
    └── Verification
             │
             ▼
      Kubernetes (Kind)
             │
     ┌───────┴────────┐
     ▼                ▼
Frontend          Backend API
     │                │
     └───────┬────────┘
             ▼
        PostgreSQL
             │
             ▼
      Prometheus Metrics
             │
             ▼
          Grafana
             │
             ▼
             Loki
```

---

# 🛠️ Technology Stack

| Category                 | Tools                     |
| ------------------------ | ------------------------- |
| Version Control          | Git, GitHub               |
| CI/CD                    | Azure DevOps Pipelines    |
| Containerization         | Docker                    |
| Container Registry       | GitHub Container Registry |
| Orchestration            | Kubernetes (Kind)         |
| Infrastructure as Code   | Terraform                 |
| Configuration Management | Ansible                   |
| Backend                  | Python Flask              |
| Frontend                 | React                     |
| Database                 | PostgreSQL                |
| Monitoring               | Prometheus                |
| Visualization            | Grafana                   |
| Logging                  | Loki                      |
| Operating System         | Ubuntu (WSL)              |

---

# 📁 Repository Structure

```text
expense-tracker-devops/
│
├── ansible/
├── backend/
├── database/
├── docker/
├── docs/
├── frontend/
├── kubernetes/
├── monitoring/
├── scripts/
├── terraform/
├── tests/
│
├── azure-pipelines.yml
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# 🌳 Git Branching Strategy

```text
main
│
└── develop
      │
      ├── feature/backend
      ├── feature/frontend
      ├── feature/docker
      ├── feature/kubernetes
      ├── feature/terraform
      └── feature/monitoring
```

* **main** → Production-ready code
* **develop** → Integration branch
* **feature/*** → Individual feature development

---

# 🚀 Planned DevOps Workflow

```text
Code
   │
   ▼
GitHub
   │
   ▼
Azure DevOps Pipeline
   │
   ├── Code Validation
   ├── Unit Tests
   ├── Docker Build
   ├── Push Image
   ├── Terraform
   ├── Kubernetes Deployment
   ├── Health Check
   └── Smoke Test
```

---

# 📅 Sprint Roadmap

| Sprint    | Objective               | Status      |
| --------- | ----------------------- | ----------- |
| Sprint 1  | Project Foundation      | ✅ Completed |
| Sprint 2  | Backend Development     | ⏳ Planned   |
| Sprint 3  | Frontend Development    | ⏳ Planned   |
| Sprint 4  | Docker Containerization | ⏳ Planned   |
| Sprint 5  | Kubernetes Deployment   | ⏳ Planned   |
| Sprint 6  | Terraform Automation    | ⏳ Planned   |
| Sprint 7  | Ansible Automation      | ⏳ Planned   |
| Sprint 8  | Azure DevOps CI/CD      | ⏳ Planned   |
| Sprint 9  | Monitoring              | ⏳ Planned   |
| Sprint 10 | Logging                 | ⏳ Planned   |
| Sprint 11 | Optimization & Testing  | ⏳ Planned   |
| Sprint 12 | Final Documentation     | ⏳ Planned   |

---

# 📊 Features (Planned)

* User Authentication
* Expense Management
* Income Tracking
* Category Management
* Dashboard & Analytics
* Monthly Reports
* Responsive UI
* REST API
* Health Check Endpoint

---

# 📈 Monitoring & Observability

The platform will include:

* Application Metrics
* Kubernetes Metrics
* Container Metrics
* Infrastructure Monitoring
* Dashboards
* Alerting (future enhancement)
* Centralized Logging

---

# 🔐 Future DevSecOps Enhancements

This project is designed so that security tooling can be integrated as the platform evolves.

Planned additions include:

* Static Application Security Testing (SAST)
* Software Composition Analysis (SCA)
* Dynamic Application Security Testing (DAST)
* Container Image Scanning
* Secret Scanning
* Kubernetes Policy Validation
* Infrastructure Security Scanning

---

# 📚 Documentation

Additional documentation is available in the `docs/` directory and will be expanded throughout each sprint.

* Architecture
* Deployment
* Monitoring
* Terraform
* Ansible
* CI/CD Pipeline
* Troubleshooting

---

# 📷 Project Screenshots

Screenshots and dashboards will be added as the project progresses.

---

# 🤝 Contributing

This repository is maintained as a portfolio project. Suggestions and improvements are welcome through issues or pull requests.

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Saravanan T H**

DevOps | DevSecOps | Cloud Security | SOC | Automation

---

⭐ If you find this project useful, consider giving it a star.