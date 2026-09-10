# Design Principles

This rule answers: **what baseline design philosophy applies when a VCO project has a user interface?**

VCO defines principles, not a mandatory UI library. Profiles ([profiles/](../profiles/)) may recommend technologies; the principles below apply regardless of stack.

## Principles

- **Minimal** — every element earns its place; remove before adding.
- **Typography-first** — hierarchy and readability come from type, not decoration.
- **Mobile-first** — design for the smallest viewport first, then enhance.
- **Accessible** — semantic structure, sufficient contrast, keyboard operability, meaningful labels. Accessibility is a requirement, not a polish step.
- **Responsive** — layouts adapt across viewports without breaking hierarchy.
- **Fast** — performance is a design property; weight and blocking work are design defects.
- **Strong hierarchy** — the user can always tell what matters most on the screen.
- **Intentional spacing** — whitespace follows a consistent scale, not eyeballing.
- **Clear states** — every interactive element has visible default, hover/focus, active, disabled, loading, empty, and error states as applicable.
- **Subtle motion** — animation communicates state change; it never merely decorates.
- **No decorative noise without purpose** — gradients, shadows, and effects require a communicative reason.

## Agent obligations

- Follow the project's existing design system or component library before introducing any new visual pattern.
- Visual changes are verifiable work: where the profile requires it, Visual QA is a verification gate (see [testing.md](testing.md)).
- Do not introduce a UI library, icon set, or font as a side effect of a task — that is a dependency decision (see [architecture.md](architecture.md)).
