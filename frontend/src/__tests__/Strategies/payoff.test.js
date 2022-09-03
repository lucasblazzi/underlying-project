import React from 'react';
import Payoff from '../../pages/Strategies/payoff';
import renderer from 'react-test-renderer';
import ReactApexChart from "react-apexcharts";

it('Página', () => {
    const tree = renderer.create(<div id="line-chart"/>).toJSON();
    expect(tree).toMatchSnapshot();
})