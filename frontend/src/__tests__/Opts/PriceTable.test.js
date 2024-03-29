import React from 'react';
import PriceTable from '../../pages/Opts/PriceTable';
import renderer from 'react-test-renderer';
import { Row, Col, Card, CardBody } from "reactstrap";

it('Página', () => {
    const tree = renderer.create(<div class = "clearfix"/>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('CardBody', () => {
    const tree = renderer.create(<CardBody />).toJSON();
    expect(tree).toMatchSnapshot();
})