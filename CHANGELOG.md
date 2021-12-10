# Changelog

<!--next-version-placeholder-->

## v0.2.0 (2021-12-10)
### Feature
* **ci:** Enable semantic release ([`ce3c79a`](https://github.com/dnikolay-ebc/FiLiP/commit/ce3c79a01a24411cce95fa5d3a8c030acf66ad54))

### Fix
* Removed typo in setup.cfg ([`557da05`](https://github.com/dnikolay-ebc/FiLiP/commit/557da05a117e807c14c89fa4703fd62dbe44333d))
* Add semantic release pipeline ([`5a76ba4`](https://github.com/dnikolay-ebc/FiLiP/commit/5a76ba4e586f607cc4a73ff3bcb3a8cad4c8f8e1))
* Added version placeholder to changelog ([`20bf979`](https://github.com/dnikolay-ebc/FiLiP/commit/20bf97970f2d1eb303066eff63e710a2285b7a97))
* Escape '*' in regex ([`01db2c4`](https://github.com/dnikolay-ebc/FiLiP/commit/01db2c467281839d148a5e27ae42a9ce70db4a2b))
* Updated QueryStatement regex to match specification ([`0f1aeb9`](https://github.com/dnikolay-ebc/FiLiP/commit/0f1aeb9a17ca4e5d68907263f2ff23738f9aa67a))

#### v0.1.8
- QuantumLeap request pagination ([#47](https://github.com/RWTH-EBC/FiLiP/issues/47))
- introduce mqtt client ([#45](https://github.com/RWTH-EBC/FiLiP/issues/45))
- introduce concurrent testing ([#41](https://github.com/RWTH-EBC/FiLiP/issues/41))
- include default values in subscription update ([#39](https://github.com/RWTH-EBC/FiLiP/issues/39))
- move back to more simple docs design ([#32](https://github.com/RWTH-EBC/FiLiP/issues/32))
- added MQTT notifications ([#24](https://github.com/RWTH-EBC/FiLiP/issues/24))
- introduced [CHANGELOG.md](https://github.com/RWTH-EBC/FiLiP/blob/development/CHANGELOG.md) with versions
- semantic model features [#30](https://github.com/RWTH-EBC/FiLiP/issues/30)
- remodeled ngsi-v2 models ([#58,#59,#60](https://github.com/RWTH-EBC/FiLiP/issues/60))
- improved ContextEntity and Device deleting methods ([#27](https://github.com/RWTH-EBC/FiLiP/issues/28))
- patch methods for ContextEntity and Device ([#74](https://github.com/RWTH-EBC/FiLiP/issues/74))

#### v0.1.7
- introduced automatic testing
([#18](https://github.com/RWTH-EBC/FiLiP/issues/18))

#### v0.1.0
- Completely reworked the structure of the library
- Added documentation  
- Use Pydantic for model validation and parsing
- Added unittests
- Configuration via environment variables, json or local
- Moved to github.com/RWTH-EBC
- Bugfix