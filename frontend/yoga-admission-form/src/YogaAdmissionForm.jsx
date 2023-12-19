import React, { useState } from 'react';
import axios from 'axios';

const YogaAdmissionForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    age: 18,
    email: '',
    contactNo: '',
    location: '',
    batch: '6-7AM',
    amount: 500,
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleAmountChange = (e) => {
    const amount = parseInt(e.target.value, 10);
    setFormData({ ...formData, amount: isNaN(amount) ? 0 : amount });
  };

  const handleEnroll = async () => {
    try {
      // Basic client-side validation
      if (formData.amount % 500 !== 0) {
        alert('Amount must be a multiple of 500.');
        return;
      }

      const response = await axios.post('http://localhost:8000', formData);

      if (response.status === 200) {
        alert(response.data.detail);

        // Uncomment the following section if you have a payment endpoint
        // const paymentResponse = await axios.post('http://your-api-endpoint/payment', {
        //   email: formData.email,
        //   amount: formData.amount,
        // });

        // if (paymentResponse.status === 200) {
        //   alert('Payment successful!');
        // } else {
        //   alert('Payment failed. Please try again.');
        // }
      } else {
        alert('Enrollment failed. Please check your details and try again.');
      }
    } catch (error) {
      console.error('Error submitting admission form:', error);
      alert('An error occurred. Please try again.');
    }
  };

  return (
    <div>
      <h1>Yoga Class Admission Form</h1>
      <label>Name:</label>
      <input type="text" name="name" value={formData.name} onChange={handleChange} />

      <label>Age:</label>
      <input type="number" name="age" value={formData.age} onChange={handleChange} />

      <label>Email:</label>
      <input type="text" name="email" value={formData.email} onChange={handleChange} placeholder="example@example.com" />

      <label>Contact Number:</label>
      <input type="text" name="contactNo" value={formData.contactNo} onChange={handleChange} />

      <label>Location:</label>
      <input type="text" name="location" value={formData.location} onChange={handleChange} />

      <label>Select Batch:</label>
      <select name="batch" value={formData.batch} onChange={handleChange}>
        <option value="6-7AM">6-7AM</option>
        <option value="7-8AM">7-8AM</option>
        <option value="8-9AM">8-9AM</option>
        <option value="5-6PM">5-6PM</option>
      </select>

      <label>Amount:</label>
      <input type="number" name="amount" value={formData.amount} onChange={handleAmountChange} min="500" step="500" />

      <p>{`The subscription of ${formData.amount} INR will be valid until ${formData.amount}`}</p>

      <button onClick={handleEnroll}>Enroll</button>
    </div>
  );
};

export default YogaAdmissionForm;
