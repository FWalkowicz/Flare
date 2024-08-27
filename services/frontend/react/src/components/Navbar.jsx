import { Link } from 'react-router-dom';
import logo from '../assets/logo.png';

export default function Navbar() {
    return (
        <nav className="bg-white fixed w-full z-20 top-0 start-0 border-b border-gray-200">
            <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
                <Link to="/" className="flex items-center space-x-3 rtl:space-x-reverse">
                    <img src={logo} className="h-8" alt="Flare Logo"/>
                    <span className="self-center text-2xl font-semibold whitespace-nowrap text-black">Flare</span>
                </Link>
                <div className="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
                    <ul className="flex flex-col p-4 md:p-0 mt-4 font-medium md:flex-row md:mt-0 md:border-0 md:bg-white">
                        <li>
                            <Link to="/model" className="block py-2 px-3 text-black hover:text-green-500">Model</Link>
                        </li>
                        <li>
                            <Link to="/dataset" className="block py-2 px-3 text-black hover:text-green-500">Dataset</Link>
                        </li>
                        <li>
                            <Link to="/train" className="block py-2 px-3 text-black hover:text-green-500">Train</Link>
                        </li>
                        <li>
                            <Link to="/predict" className="block py-2 px-3 text-black hover:text-green-500">Predict</Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
}
