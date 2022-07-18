import React from 'react';
import renderer from 'react-test-renderer';
import personal from '../../pages/Strategies/personal';
import { Row, Col, Card, CardBody } from "reactstrap";

it('Página', () => {
    const tree = renderer.create(<div class = "page-content"/>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('CardBody', () => {
    const tree = renderer.create(<CardBody />).toJSON();
    expect(tree).toMatchSnapshot();
})