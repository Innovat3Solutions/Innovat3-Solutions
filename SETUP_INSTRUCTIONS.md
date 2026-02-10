
# Integration Instructions

The components have been created in `components/ui/navigation-menu.tsx` and `components/NavigationMenuDemo.tsx`.

 However, **your current project appears to be a static HTML/CSS/JS project**, while the components provided are **React** components that require a build process (like Next.js or Vite), Tailwind CSS, and specific dependencies.

To fully integrate these components, you need to set up a React environment.

## Option 1: Migrate to Next.js (Recommended for Shadcn UI)

1.  **Initialize a new Next.js project:**
    ```bash
    npx create-next-app@latest my-app --typescript --tailwind --eslint
    ```
2.  **Navigate into the directory:**
    ```bash
    cd my-app
    ```
3.  **Initialize Shadcn UI:**
    ```bash
    npx shadcn-ui@latest init
    ```
4.  **Install Text/UI Dependencies:**
    ```bash
    npm install @radix-ui/react-icons @radix-ui/react-navigation-menu class-variance-authority lucide-react clsx tailwind-merge
    ```
5.  **Move the files:**
    Copy `components/ui/navigation-menu.tsx` and `components/NavigationMenuDemo.tsx` into your new project's component folder.

## Option 2: Setup Vite + React

1.  **Create a Vite app:**
    ```bash
    npm create vite@latest my-app -- --template react-ts
    ```
2.  **Install Tailwind:**
    Follow the official Tailwind guide for Vite.
3.  **Install Dependencies:**
    ```bash
    npm install @radix-ui/react-icons @radix-ui/react-navigation-menu class-variance-authority lucide-react clsx tailwind-merge
    ```

## Dependencies Review

The following dependencies are required for the newly added components:
*   `@radix-ui/react-icons`
*   `@radix-ui/react-navigation-menu`
*   `class-variance-authority`
*   `clsx`
*   `tailwind-merge`
*   `radix-ui` (primitive)

## Current Status

*   `components/ui/navigation-menu.tsx`: **Created**
*   `components/NavigationMenuDemo.tsx`: **Created**

**Note:** These files will NOT work in your `index.html` file directly. You must use a React build tool.
