import React from "react";
import Link from "next/link";
import Layout from "@/components/layout/Layout";
import PageHead from "@/components/layout/PageHead";

function About() {
  return (
    <>
      <Layout>
        <PageHead headTitle="FAQs"></PageHead>
        <div>
          <h1 className="text-center text-danger">Help</h1>
        </div>
      </Layout>
    </>
  );
}

export default About;
