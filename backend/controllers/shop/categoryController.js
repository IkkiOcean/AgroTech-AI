const Category = require('../../model/shop/category');

// Get all categories
exports.getAllCategories = async (req, res) => {
  try {
    const categories = await Category.find();
    res.json(categories);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Get category by ID
exports.getCategoryById = async (req, res) => {
  try {
    const category = await Category.findById(req.params.id);
    if (!category) return res.status(404).json({ error: "Category not found" });
    res.json(category);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Create new category
exports.createCategory = async (req, res) => {
  console.log(req.body);
  const categories = req.body; // Expecting an array of { name, description }

  if (!Array.isArray(categories)) {
    return res.status(400).json({ error: "Input should be an array of categories." });
  }

  try {
    const savedCategories = await Category.insertMany(categories);
    res.status(201).json(savedCategories);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Update category
exports.updateCategory = async (req, res) => {
  try {
    const updatedCategory = await Category.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.json(updatedCategory);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Delete category
exports.deleteCategory = async (req, res) => {
  try {
    await Category.findByIdAndDelete(req.params.id);
    res.json({ message: "Category deleted" });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
