# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- New feature or enhancement that is yet to be released.

### Changed
- Descriptions of changes that modify existing behavior.

### Fixed
- Bug fixes made to the project.

### Deprecated
- Features that are deprecated and will be removed in future releases.

### Removed
- Features that were removed in this release.

### Security
- Vulnerabilities or security-related changes.

---

## [v13.0.2] - 2024-12-04

### Changed/ Fixed
- **Security/ CI-flow**: Reverted changes for packages updated in application because of crash at build, dependencies not working for other packages.

## [v13.0.1] - 2024-12-02

### Added
- **Workflow/ Security**: Added security.yml for the CI flow and security aspects of the application. Also re-done some work for ansible code, added more seucrity features for example, SSH and access to servers.

## [v12.2.3] - 2024-11-28

### Added
- **Ansible/ Routes**: Finished CD flow for ansible and connection between github and azure. Added site for version control and added tests to verify that /version is up and running, tests can be found in playbook and as an integration test.

## [v12.1.0] - 2024-11-22

### Added
- **Ansible**: Fixed files for ansible setup environment setup and loadbalancer installation.

## [v11.3.0] - 2024-11-12

### Added
- **Release**: Added new release for project.

## [v11.2.0] - 2024-11-12

### Added
- **DockerFiles**: Added docker implementation and yml for tests and to spin-up test environment.


## [v11.1.0] - 2024-11-11

### Added
- **Followers**: Added functionality to follow users blogposts.

## [v11.0.0] - 2024-11-07

### Added
- **commit-files**: Added commit-files to be able to write a commit-message using a template

