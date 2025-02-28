# Typora Semi-Automated License Bypass

I AM not good at English.

Sorry.

A tool to eliminate Typora activation pop-ups and watermark displays.

中文说明请戳[这里](README_CN.md)

## Warnings

⚠️ **This patch is strictly for educational and research purposes!**

- Users must delete all related files within 24 hours of download. Support genuine software through official purchases.
- Commercial use or illegal applications are strictly prohibited.
- Developers disclaim all liability for damages or legal consequences arising from misuse.
- No warranties apply regarding functionality, accuracy, or reliability.
- Reverse engineering or unauthorized distribution violates terms of use.

## Technical Overview

- Originally compatible with Typora v1.10.6 (Linux ARM64) through binary patching
- Implements resource file modification concepts from deprecated typora-cracker project
- Bypasses compiled JS validation through reverse engineering techniques
- Side effect: Disables manual license window access

## Implementation Notes

- Incompatible with Typora v1.10.8+ due to checksum changes
- Requires Python environment setup (`pip install -r requirements.txt`)
- Modify File
  ```shell
  python3 typora.py {installRoot}/Typora/resources/app.asar
  ```

#### Modify File

Critical JS modification in /resources/page-dist/static/js/License* files:

```shell
- e.hasActivated="true"==e.hasActivated
+ e.hasActivated="true"!=e.hasActivated
```

## LICENSE

MIT LICENSE