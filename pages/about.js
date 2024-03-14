import Link from "next/link";
import React from "react";
import Layout from "@/components/layout/Layout";

const About = () => {
  return (
    <>
      <Layout>
        <section className="section">
          <div className="container col text-center">
            <h1 className="text-primary-emphasis">Proje Geliştiricileri</h1>
            <ul className="list-unstyled d-flex mt-5">
              <li className="col">
                <Link
                  href="https://github.com/leidorf"
                  className="text-info nav-link mb-4"
                >
                  <img alt="Güray Dağ" src="/assets/imgs/guray-dag.png"></img>
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
                >
                  <img alt="Veli Yarar" src="/assets/imgs/veli-yarar.png"></img>
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
