# env.setup

Ansible collection for setting up essential tools, user environments, and folder structures on a fresh Linux system.

---

## Overview

`env.setup` helps automate the setup of a personal or dev environment by organizing multiple setup steps into clean, reusable roles.

This collection was originally based on 5 standalone playbooks, and is now refactored into **3 modular roles** for improved maintainability and reuse.

---

## Roles Included

| Role               | Description |
|--------------------|-------------|
| `folder_tasks`     | Sets up a working directory and manages local backups. |
| `tools_install`    | Installs key packages (like mtools or other essential tools). |
| `system_config`    | Creates a user based on hostname and appends a welcome signature to `.bashrc`. |

---

## Quick Start

### 1. Install the Collection

from a local tarball:

```bash
ansible-galaxy collection install env-setup-1.0.0.tar.gz
```

Or from GitHub:

```yaml
# requirements.yml
collections:
  - name: env.setup
    source: https://github.com/omarmohsen9/env.setup.git
    type: git
    version: main
```

```bash
ansible-galaxy collection install -r requirements.yml
```
(Ansible Galaxy installation currently not supported)

### 2. Example Playbook
```yaml
# setup.yml
- hosts: all
  become: true
  collections:
    - env.setup

  roles:
    - folder_manage
    - tools_install
    - system_config
```

then run:
```bash
ansible-playbook -i inventories/inv.ini setup.yml
```

## Folder Structure

```bash
env.setup/
├── docs/
├── meta/
├── playbooks/
├── plugins/
│   └── modules/
└── roles/
    ├── folder_manage/
    │   ├── defaults/
    │   └── tasks/
    ├── system_config/
    │   ├── defaults/
    │   └── tasks/
    └── tools_install/
        ├── defaults/
        └── tasks/
```

## License
MIT License © 2025 Omar Mohsen
