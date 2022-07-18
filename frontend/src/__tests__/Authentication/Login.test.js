import React from 'react';
import Login from '../../pages/Authentication/Login';
import renderer from 'react-test-renderer';
import { Row, Col, Alert, Card, CardBody, Container } from "reactstrap";
import { AvForm, AvField } from "availity-reactstrap-validation"

it('Form', () => {
    const tree = renderer.create(<AvForm/>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('CardBody', () => {
    const tree = renderer.create(<CardBody />).toJSON();
    expect(tree).toMatchSnapshot();
})