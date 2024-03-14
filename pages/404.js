import Link from "next/link";
import React from "react";
import Layout from "@/components/layout/Layout";

const Error = () => {
  return (
    <>
      <Layout>
        <section className="section">
          <div className="container">
            <h1 className="text-center text-weight-bold text-danger">
              404
              <br /> Böyle bir sayfa bulunamadı!
            </h1>
          </div>
        </section>
      </Layout>
    </>
  );
};

export default Error;
