import React from 'react';
import UserProfile from '../pages/pages-404';
import renderer from 'react-test-renderer';
import { Container, Row, Col } from "reactstrap"

it('Página', () => {
    const tree = renderer.create(<Container/>).toJSON();
    expect(tree).toMatchSnapshot();
})