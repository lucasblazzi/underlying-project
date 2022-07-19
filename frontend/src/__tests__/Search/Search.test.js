import React from 'react';
import Search from '../../pages/Search/index';
import renderer from 'react-test-renderer'
import { Row, Col, Card, CardBody, CardImg, Container, Input, Button, Table, Spinner, InputGroup, InputGroupAddon } from "reactstrap";
import { render, fireEvent, getByLabelText } from '@testing-library/react';

it('Página', () => {
    const tree = renderer.create(<div className="page-content"></div>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('Barra de busca', () => {
    const tree = renderer.create(<Input id="busca"></Input>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('Resultado de pesquisa', () => {
    const tree = renderer.create(<Row id="load"></Row>).toJSON();
    expect(tree).toMatchSnapshot();
})