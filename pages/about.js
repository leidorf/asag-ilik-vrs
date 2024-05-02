import Link from "next/link";
import React from "react";
import Layout from "@/components/layout/Layout";
import PageHead from "@/components/layout/PageHead";

const About = () => {
  return (
    <>
      <Layout>
        <PageHead headTitle="About Us"></PageHead>
        <section className="section">
          <div className="container col text-center">
            <h1 className="text-primary-emphasis">Proje Geliştiricileri</h1>
            <ul className="list-unstyled d-flex mt-5">
              <li className="col">
                <Link
                  href="https://github.com/leidorf"
                  className="text-info nav-link mb-4"
                  target="_blank"
                >
                  <img alt="Güray Dağ" style={{ width: "400px" }} src="https://avatars.githubusercontent.com/u/93585259?v=4"></img>
                </Link>
                <h5>
                  Güray Dağ <br />
                  (Web Developer)
                </h5>
              </li>
              <li className="col">
                <Link
                  href="https://github.com/VeliYarar"
                  className="text-info nav-link mb-4"
                  target="_blank"
                >
                  <img alt="Veli Yarar" style={{ width: "400px" }} src="https://avatars.githubusercontent.com/u/95528034?v=4"></img>
                </Link>
                <h5>
                  Veli Yarar <br />
                  (AI Developer)
                </h5>
              </li>
            </ul>
          </div>
        </section>
      </Layout>
    </>
  );
};

export default About;
