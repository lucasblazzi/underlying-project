import React from 'react';
import MarketTable from '../../pages/Opts/MarketTable';
import renderer from 'react-test-renderer'
import { Row, Col, Card, CardBody } from "reactstrap";

it('Página', () => {
    const tree = renderer.create(<CardBody/>).toJSON();
    expect(tree).toMatchSnapshot();
})