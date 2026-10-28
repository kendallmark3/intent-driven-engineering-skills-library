# Security

Agent Skills are executable instructions from the agent's perspective and are part of the repository trust boundary.

This library's included scripts only validate and package local files. They do not call networks, read credentials, modify external systems, or delete user data.

Before accepting Skill changes, review:

- commands the Skill asks the agent to run;
- network or external service access;
- secret and credential handling;
- package installation;
- destructive file/system operations;
- tool permissions;
- instructions that bypass policy, tests, review, or evidence.

Report security issues privately to the repository owner before public disclosure.
