import React from 'react';
import renderer from 'react-test-renderer'
import { Row, Col, Card, CardBody, Input } from "reactstrap";
import SearchBar from '../../pages/Strategies/SearchBar';

it('Página', () => {
    const tree = renderer.create(<SearchBar/>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('Barra Pesquisa', () => {
    const tree = renderer.create(<Input id="busca" />).toJSON();
    expect(tree).toMatchSnapshot();
})

it('Resultado Pesquisa', () => {
    const tree = renderer.create(<Row id="load" />).toJSON();
    expect(tree).toMatchSnapshot();
})