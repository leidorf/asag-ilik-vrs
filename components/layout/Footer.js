import Link from "next/link";
import React from "react";

const Footer = () => {
  return (
    <>
      <div class="container footer">
        <footer class="py-3 my-4">
          <ul class="nav justify-content-center border-bottom pb-3 mb-3">
            <li class="nav-item">
              <Link href="/" class="nav-link px-2 text-primary-emphasis">
                Ana Sayfa
              </Link>
            </li>
            <li class="nav-item">
              <Link href="/voice-recognition" class="nav-link px-2 text-primary-emphasis">
                Ses Tanıma
              </Link>
            </li>
            <li class="nav-item">
              <Link href="/help" class="nav-link px-2 text-primary-emphasis">
                Nasıl Kullanılır
              </Link>
            </li>
            <li class="nav-item">
              <Link href="/about" class="nav-link px-2 text-primary-emphasis">
                Hakkımızda
              </Link>
            </li>
          </ul>
          <p class="text-center text-body-secondary">
            &copy; 2024 asag-ilik-vrs
          </p>
        </footer>
      </div>
    </>
  );
};

export default Footer;
