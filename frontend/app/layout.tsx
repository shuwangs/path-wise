import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "PathWise",
  description: "An evidence-grounded career assistant",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
