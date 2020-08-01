import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.css';

function App() {
	const [item, setItem] = useState([]);
	const [description, setDescription] = useState('');
	const [loading, setLoading] = useState(false);

	useEffect(() => {
		axios
			.get('https://job-description-scanner.herokuapp.com/results')
			.then(async (res) => {
				const data = await res.data;
				setItem(data);
			});
		console.log('render');
	}, []);

	const newDescription = (e) => {
		setDescription(e.target.value);
	};

	const itemRef = useRef(item);
	itemRef.current = item;

	return (
		<div className='App'>
			<form
				style={{ height: '500px', margin: 'auto' }}
				method='POST'
				action='https://job-description-scanner.herokuapp.com/process'>
				<label>Enter Description</label>
				<input
					type='text'
					value={description}
					onChange={newDescription}
					name='description'
					style={{ height: '200px', margin: 'auto' }}
				/>
				<button type='submit'>Submit</button>
			</form>
			<div>Results</div>
			<div
				style={{
					display: 'flex',
					justifyContent: 'space-evenly',
					flexFlow: 'column',
				}}>
				{item !== []
					? item.map((word, i) => (
							<div
								style={{ display: 'flex', justifyContent: 'center' }}
								key={i}>
								<div key={word} style={{ width: '30%' }}>
									<p style={{ textAlign: 'left' }}>{word[0]}</p>
								</div>
								<div>
									<p>{word[1]}</p>
								</div>
							</div>
					  ))
					: ''}
			</div>
		</div>
	);
}

export default App;
