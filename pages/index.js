import Link from "next/link";
import React, { useState } from "react";
import Layout from "../components/layout/Layout";
import PageHead from "@/components/layout/PageHead";

const HomePage = () => {
  return (
    <>
      <Layout>
        <PageHead headTitle="Home Page"></PageHead>
        <div>
          <h1 className="text-center text-primary-emphasis">ANA SAYFA</h1>
        </div>
      </Layout>
    </>
  );
};

export default HomePage;
