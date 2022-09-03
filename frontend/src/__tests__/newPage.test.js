import React from 'react';
import UserProfile from '../pages/newPage';
import renderer from 'react-test-renderer';

it('Página', () => {
    const tree = renderer.create(<div className="page-content"/>).toJSON();
    expect(tree).toMatchSnapshot();
})