import React from 'react';
import SharedStrategies from '../../pages/Strategies/shared';
import renderer from 'react-test-renderer'
import { Row, Col, Card, CardBody, Input } from "reactstrap";

it('Página', () => {
    const tree = renderer.create(<div class = "page-content"/>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('CardBody', () => {
    const tree = renderer.create(<CardBody />).toJSON();
    expect(tree).toMatchSnapshot();
})