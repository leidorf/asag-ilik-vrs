import Link from "next/link";
import React, { useEffect, useState } from "react";

const Header = () => {
  return (
    <>
      <div className="container">
        <header className="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
          <Link
            href="/"
            className="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none"
          >
            <img className="bi me-2" src="/assets/imgs/logo.png" style={{width: "45px" }} ></img>
            <span className="fs-4 text-primary-emphasis">Ses Tanıma Sistemi</span>
          </Link>

          <ul className="nav nav-pills">
            <li className="nav-link ">
              <Link href="/" className="nav-link active">
                Ana Sayfa
              </Link>
            </li>
            <li className="nav-link">
              <a href="/voice-recognition" className="nav-link text-primary-emphasis">
                Ses Tanıma
              </a>
            </li>
            <li className="nav-link">
              <Link href="/help" className="nav-link text-primary-emphasis">
                Nasıl Kullanılır
              </Link>
            </li>
            <li className="nav-link">
              <Link href="/about" className="nav-link text-primary-emphasis">
                Hakkımızda
              </Link>
            </li>
          </ul>
        </header>
      </div>
    </>
  );
};

export default Header;
