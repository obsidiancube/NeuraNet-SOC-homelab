# NeuraNet-SOC-homelab
NueraNet-SOC

Project Status

A scalable, AI-driven cybersecurity homelab and Security Operations Center (SOC) built to demonstrate advanced threat detection, penetration testing, and system orchestration using virtual machines (VMs) and custom AI agents.
Overview

NueraNet-SOC is an ambitious personal project designed to showcase expertise in cybersecurity, AI integration, and solutions architecture. This homelab simulates a miniature enterprise security environment, featuring a SOC for threat monitoring, a penetration testing suite for ethical hacking, and AI agents to automate and enhance security workflows. Initially built on a single host with VMware virtualization, it’s designed to scale up with advanced hardware (e.g., NVIDIA DGX) for deeper AI capabilities.
Goals

    Build a functional SOC with AI-driven threat detection and reporting.
    Automate penetration testing workflows using AI agents.
    Create a modular, scalable architecture documented via GitHub.
    Serve as a portfolio piece for transitioning into cybersecurity and solutions architect roles.

Current Hardware

    Host OS: Parrot OS (Linux-based, security-focused)
    RAM: 32GB
    Storage: 800GB free
    CPU: Core i7 (multi-core with hyper-threading)
    Virtualization: VMware Workstation

Future Vision

Scale to enterprise-grade hardware (e.g., NVIDIA DGX) and integrate deep learning models for advanced threat analysis.
Architecture

The homelab consists of multiple VMs, each serving a distinct role, connected via a virtual network:

    SOC VM
        Purpose: Centralized monitoring and threat detection.
        Tools: Wazuh (SIEM), Python-based AI anomaly detection.
        AI Agent: Analyzes logs and network traffic for anomalies.
    Penetration Testing VM
        Purpose: Simulate ethical hacking and vulnerability scanning.
        Tools: Parrot OS (or Kali Linux), Metasploit, Nmap.
        AI Agent: Automates attack scripting and result analysis.
    Target VM
        Purpose: Vulnerable system for testing attacks.
        Tools: Metasploitable, DVWA (Damn Vulnerable Web App).
    AI Agent Controller VM
        Purpose: Coordinates AI agents across the homelab.
        Tools: Python, TensorFlow/PyTorch, Flask API.
    Network Simulation VM
        Purpose: Simulates network routing and firewalling.
        Tools: pfSense.

Diagram
