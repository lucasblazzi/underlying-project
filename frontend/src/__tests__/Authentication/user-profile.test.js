import React from 'react';
import UserProfile from '../../pages/Authentication/user-profile';
import renderer from 'react-test-renderer';
import { Row, Col, Alert, Card, CardBody, Container } from "reactstrap";
import { AvForm, AvField } from "availity-reactstrap-validation";

it('Página', () => {
    const tree = renderer.create(<div className="page-content"/>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('CardBody', () => {
    const tree = renderer.create(<CardBody />).toJSON();
    expect(tree).toMatchSnapshot();
})

it('Form', () => {
    const tree = renderer.create(<AvForm/>).toJSON();
    expect(tree).toMatchSnapshot();
})