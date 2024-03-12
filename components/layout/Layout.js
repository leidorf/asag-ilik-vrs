import React, { useState } from 'react';

const Layout = ({ children }) => {
    const [openClass, setOpenClass] = useState('');

    return (
        <>
            <main className="main">
                {children}
            </main>

        </>
    );
};

export default Layout;