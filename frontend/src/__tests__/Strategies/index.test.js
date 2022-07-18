import React from 'react';
import Strategies from '../../pages/Strategies/index';
import renderer from 'react-test-renderer';
import { Row, Col, Card, CardBody, Container, Input, Spinner, Button, Collapse, Modal, Label } from "reactstrap";
import SearchBar from "../../pages/Strategies/SearchBar";

it('Página', () => {
    const tree = renderer.create(<div className="page-content"></div>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('CardBody', () => {
    const tree = renderer.create(<CardBody />).toJSON();
    expect(tree).toMatchSnapshot();
})