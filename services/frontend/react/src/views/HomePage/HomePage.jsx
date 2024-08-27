import React from 'react';
import home_bg from '../../assets/home_bg.jpg';
import how_it_works from "../../assets/how_it_works.png"
import architecture from '../../assets/architecture.png';
import ml_logo from '../../assets/ml_logo.png';

export default function HomePage() {
    return (
        <>
            <div className="h-[50vh] overflow-hidden relative">
                <img
                    className="w-full h-auto absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
                    src={home_bg}
                    alt="just a photo"
                />
            </div>
            <div className="grid gap-4 grid-cols-3 grid-rows-1 pt-16 flex flex-col justify-center items-center text-center pb-20">
                <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-green-600">Kluczowa Funkcja Naszej Aplikacji</h1>
                <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-green-600">Jak to działa?</h1>
                <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-green-600">Architektura</h1>
                <div className="flex flex-col justify-center items-center text-center">
                    <p className="mb-6 text-lg font-normal">
                        W obliczu dynamicznego rozwoju uczenia maszynowego, kluczowe staje się szybkie i efektywne opracowywanie, trenowanie oraz wdrażanie modeli.
                        Nasza aplikacja oferuje nowoczesne podejście do zarządzania cyklem życia modeli dzięki metodologii MLOps, inspirowanej praktykami DevOps.
                        Integrując automatyzację, uczenie maszynowe i inżynierię danych, zapewniamy lepsze, długoterminowe wyniki i zwiększoną produktywność.
                        Dzięki naszej platformie, użytkownicy mogą łatwo edytować zbiory danych, wybierać modele, dostosowywać hiperparametry, a następnie trenować
                        modele i przeprowadzać predykcje – wszystko w jednym miejscu.
                    </p>
                    <img
                        className="mb-6 text-lg font-normal h-max"
                        src={ml_logo}
                        alt="just a photo"
                    />
                </div>
                <div className="flex flex-col justify-center items-center text-center">
                    <img
                        className="mb-6 text-lg font-normal h-max"
                        src={how_it_works}npm
                        alt="just a photo"
                    />
                </div>
                <div className="flex flex-col justify-center items-center text-center">
                    <img
                        className="mb-6 text-lg font-normal h-auto "
                        src={architecture}
                        alt="just a photo"
                    />
                </div>
            </div>
        </>
    )
}
