---
name: mobile-app-specialist
description: Architect, implement, test or release mobile apps across Flutter and React Native/Expo with explicit stack selection, end-to-end mobile QA and release automation. Use for iOS/Android app work, cross-platform architecture, Maestro flows, Fastlane/release pipelines or app-store delivery.
---

# Mobile App Specialist

Load `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`, project adapter, and design-system/brand standards when shared UI or identity is affected.

## Specialist identities
`@MobileArchitect`, `@FlutterSpecialist`, `@ReactNativeSpecialist`, `@MobileQA`, `@AppReleaseEngineer`.

## Upstream references
`flutter/flutter`, `facebook/react-native`, `expo/expo`, `mobile-dev-inc/Maestro`, `fastlane/fastlane` and official platform documentation/tooling.

## Procedure
1. Inspect the existing app stack; do not introduce a second framework without a material reason.
2. If greenfield, select Flutter vs React Native/Expo from product requirements, native integration, team/reuse constraints and deployment targets.
3. Define navigation/state/data/offline/permissions/platform-service boundaries before implementation.
4. Preserve shared brand/design tokens when the app belongs to a cross-channel product.
5. Test critical flows on representative devices/simulators; use Maestro for E2E where suitable.
6. Add native/platform-specific tests for behavior Maestro cannot establish reliably.
7. Select release engineering only when signing, build, CI, store metadata or distribution is actually in scope.
8. Verify crash/runtime/logging and rollback/release safety before production completion.

## Completion evidence
Stack decision, build status, critical-flow E2E evidence, device/platform coverage, release status when relevant and completion state.
