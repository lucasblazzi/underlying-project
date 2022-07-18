import React from 'react';
import Dashboard from '../../pages/Dashboard/index';
import renderer from 'react-test-renderer'

it('Página', () => {
    const tree = renderer.create(<div class = "page-content"/>).toJSON();
    expect(tree).toMatchSnapshot();
})