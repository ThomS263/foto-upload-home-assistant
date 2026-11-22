# Security policy

Security fixes are provided for the latest revision of the integration and add-on. Report suspected vulnerabilities privately to the repository owner and do not create a public issue containing exploitable details, server addresses, access tokens, passwords, diagnostics or real photos.

Include the affected Home Assistant, Foto-Upload integration and add-on versions, reproduction steps and expected impact. Update to the current revision before reporting an issue that only affects an older test build.

The integration polls the configured Foto-Upload server locally and stores its URL in the Home Assistant configuration entry. It does not store album or administrator passwords. The add-on inherits the Foto-Upload server security model documented in the upstream repository.
