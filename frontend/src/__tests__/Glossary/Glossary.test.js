import React from 'react';
import Glossary from '../../pages/Glossary/index';
import renderer from 'react-test-renderer'
import {Container} from "reactstrap"

it('Página', () => {
    const tree = renderer.create(<div class = "page-content"/>).toJSON();
    expect(tree).toMatchSnapshot();
})

it('Container', () => {
    const tree = renderer.create(<Container/>).toJSON();
    expect(tree).toMatchSnapshot();
})