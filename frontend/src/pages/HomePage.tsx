import React from 'react';

const years = Array(59).fill({
    year: 1788,
    // image: 'https://upload.wikimedia.org/wikipedia/commons/a/a9/ElectoralCollege1912.svg',
    image: 'https://en.wikipedia.org/wiki/File:ElectoralCollege1916.svg'
});

const HomePage: React.FunctionComponent = () => {
    return (
        <div className="py-12 bg-white">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="lg:text-center">
                    <p className="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
                        US Presidential Election History
                    </p>
                    <p className="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
                        1788-2020
                    </p>
                </div>

                <div className="mt-10">
                    <dl className="space-y-10 md:space-y-0 md:grid md:grid-cols-3 md:gap-x-8 md:gap-y-10">
                        {years.map((year, index) => (
                            <div key={year.year + (index * 4)} className="relative">
                                <img alt={`View of the US results for the year ${year.year}`} src={year.image}/>
                                <dt>
                                    <p className="ml-16 text-lg leading-6 font-medium text-gray-900">{year.year + (index * 4)}</p>
                                </dt>
                            </div>
                        ))}
                    </dl>
                </div>
            </div>
        </div>
    )
}

export default HomePage;
